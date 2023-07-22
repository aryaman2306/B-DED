#this code can prevent ransomware attack by monitoring the files 
import os

def monitor_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.encrypted'):
            # Ransomware detected, take action
            print(f"Ransomware detected: {filename}")
            # Remove encrypted file
            os.remove(os.path.join(directory, filename))
            # Restore original file from backup
            os.rename(os.path.join(directory, f"{filename[:-10]}.backup"), os.path.join(directory, filename[:-10]))

if __name__ == '__main__':
    # Monitor files in specified directory
    monitor_files('/path/to/directory')
