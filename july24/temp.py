
import matlab.engine
eng = matlab.engine.start_matlab()



eng.addpath(r'/Users/jamkabeeralikhan/Documents/MATLAB')

d = 2
result = eng.Optimizer(d - 1)

# Print the result
print(f"The result is: {result}")

# Close the MATLAB engine
eng.quit()