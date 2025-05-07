from pycomm3 import CIPDriver

def main():
    ip = "172.18.0.2"  # Server IP
    path = f"tcp://{ip}/44818"

    try:
        with CIPDriver(path) as plc:
            print("Connected to PLC")
            # Example read (you can customize this tag based on your PLC setup)
            result = plc.read_tag("MyTag")
            print(f"Tag Value: {result.value}")

    except Exception as e:
        print(f"Error connecting to PLC: {e}")

if __name__ == "__main__":
    main()