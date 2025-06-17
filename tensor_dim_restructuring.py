import torch

# Dimensions for the tensor
a = 2     # Batch size dimension
b = 2     # Number of rows in the tensor
c = 8     # Number of columns in the tensor

# Create a tensor of shape (2, 2, 8) filled with random values
tensor = torch.rand(a, b, c) # (2, 2, 8)

#print(tensor)

# Temporary tensors to hold intermediate values
temp1 = torch.zeros(b * 2)                      # Temporary variable to hold the new vector (1x4)
temp2 = torch.zeros(c, b * 2)                   # Temporary variable to hold the 8x4 matrix
output_tensor = torch.zeros(a // 2, c, b * 2)   # Final output tensor to hold the result (1x8x4)

# Function to perform the inner loop logic and return a 1x4 vector
def inner_loop(m, i):
    # Define the range of batches to process
    l1 = 2 * i
    l2 = 2 * (i + 1)
    
    # Loop through the batches for the given range
    for l in range(l1, l2):
        # For the first batch in the pair, fill temp1 with data from the tensor
        if l == l1:
            for k in range(a):
                temp1[k] = tensor[l][k][m]
        # For the second batch in the pair, fill the rest of temp1
        else:
            for k in range(a):
                temp1[k + a] = tensor[l][k][m]
    
    return temp1  # Returns the 1x4 vector

# Function to perform the second loop and return the 8x4 matrix
def inner_second_loop(i):
    for j in range(c):
        # Call the inner loop for each column in the tensor, generating a 8x4 matrix
        temp2[j] = inner_loop(j, i)
    
    return temp2  # Returns the 8x4 matrix

# Main logic to fill the output_tensor
for i in range(a // 2):
    # For each pair of batches in the tensor, fill the output_tensor
    output_tensor[i] = inner_second_loop(i)  # Writes 1x8x4 to output_tensor

# Print the final output tensor
print(output_tensor)
