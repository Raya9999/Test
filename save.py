import numpy as np

# Đường dẫn đến tệp CSV
csv_file = "path/to/output.csv"

# Ghi features_array vào tệp CSV
np.savetxt(csv_file, features_array, delimiter=',')
