import firebase_admin
from firebase_admin import credentials, db
import pandas as pd
import numpy as np
import time
import os

# TensorFlow ki faaltu warnings ko hide karne ke liye
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from sklearn.preprocessing import MinMaxScaler

print("[SYSTEM] Booting Deep Learning Core (LSTM)...")

# 1. Firebase se connect karna (Apni key ka naam dhyan rakhein)
cred = credentials.Certificate("firebase-keys.json") 
firebase_admin.initialize_app(cred, {'databaseURL': 'Add Data Base Url here'})

scaler = MinMaxScaler(feature_range=(0, 1))

# Time-Series ke liye data sequences banana (Pichle 5 readings se agli 1 predict karna)
def create_sequences(data, seq_length):
    X, y = [], []
    for i in range(len(data) - seq_length):
        X.append(data[i:(i + seq_length)])
        y.append(data[i + seq_length])
    return np.array(X), np.array(y)

while True:
    try:
        print("\n[AI KERNEL] Fetching History for Deep Learning...")
        history_ref = db.reference('history')
        historical_data = history_ref.get()

        if historical_data and len(historical_data) > 10:
            # Sirf temperature nikalna history se
            temp_list = [v['temperature'] for k, v in historical_data.items() if 'temperature' in v]
            
            # 2. Data Prepare Karna LSTM ke liye
            df = pd.DataFrame(temp_list, columns=['Temperature'])
            scaled_data = scaler.fit_transform(df)
            
            seq_length = 5 if len(scaled_data) > 6 else len(scaled_data) - 2
            X, y = create_sequences(scaled_data, seq_length)
            
            # Reshape for LSTM [samples, time steps, features]
            X = np.reshape(X, (X.shape[0], X.shape[1], 1))

            # 3. Build LSTM Neural Network (Deep Learning Model)
            model = Sequential()
            model.add(LSTM(50, activation='relu', input_shape=(seq_length, 1)))
            model.add(Dense(1))
            model.compile(optimizer='adam', loss='mse')
            
            print(f"[AI KERNEL] Training LSTM Network on {len(df)} records...")
            # Epochs=10 ka matlab model data ko 10 baar padhega accurate hone ke liye
            model.fit(X, y, epochs=10, batch_size=2, verbose=0)
            print("[AI KERNEL] Training Complete.")

            # 4. Live Prediction and Early Warning Logic
            live_ref = db.reference('incubator')
            live_data = live_ref.get()
            
            if live_data and 'temp' in live_data:
                recent_temps = temp_list[-seq_length:]
                if len(recent_temps) == seq_length:
                    recent_scaled = scaler.transform(np.array(recent_temps).reshape(-1, 1))
                    recent_reshaped = np.reshape(recent_scaled, (1, seq_length, 1))
                    
                    # AI Predicts Future Temperature
                    predicted_scaled = model.predict(recent_reshaped, verbose=0)
                    future_temp = round(scaler.inverse_transform(predicted_scaled)[0][0], 2)
                    
                    print(f"[PREDICTION] Target Horizon T-Core: {future_temp}°C")

                    # Medical Anomaly Alert Logic
                    ml_warning = "LSTM FORECAST: STABLE TRAJECTORY"
                    if future_temp < 35.0: 
                        ml_warning = "CRITICAL: HYPOTHERMIA TRAJECTORY DETECTED!"
                    elif future_temp > 37.5: 
                        ml_warning = "WARNING: OVERHEATING TRAJECTORY DETECTED!"

                    # 5. Push Future Data back to Dashboard
                    db.reference('incubator/ml_prediction').set({
                        'future_temp': future_temp,
                        'ml_alert': ml_warning
                    })
                    print("[CLOUD] Deep Learning projection synced with Dashboard.")
            else:
                print("[WARNING] Live sensor data missing.")
        else:
            print("[WARNING] Gathering data... LSTM requires minimum 10 historical records.")

    except Exception as e:
        print(f"[FATAL ERROR] {e}")

    # Har 15 second mein model khud ko re-train karega naye data par
    time.sleep(15)
