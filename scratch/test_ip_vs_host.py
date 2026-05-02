import time
import MySQLdb

def test_raw_connect(host):
    print(f"Testing raw MySQLdb connection to {host}...")
    start = time.time()
    try:
        conn = MySQLdb.connect(
            host=host,
            user="root",
            passwd="BpVHOwwuFkxGPiimgcHhpyMgjRGFehxe",
            db="railway",
            port=31786
        )
        end = time.time()
        print(f"Connection to {host} took: {end - start:.4f} seconds")
        conn.close()
    except Exception as e:
        print(f"Error connecting to {host}: {e}")

if __name__ == "__main__":
    test_raw_connect("switchyard.proxy.rlwy.net")
    test_raw_connect("66.33.22.232")
