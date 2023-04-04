import os
# Function to rename multiple files
def main():
	i = 459
	path="C:\\Users\\pratham sharma\\Desktop\\Lung_Cancer\\Data\\train\\squamous.cell.carcinoma_left.hilum_T1_N2_M0_IIIa\\"
	for filename in os.listdir(path):
		my_dest ="Train_" + str(i) + ".png"
		my_source =path + filename
		my_dest =path + my_dest
		# rename() function will
		# rename all the files
		os.rename(my_source, my_dest)
		i += 1
# Driver Code
if __name__ == '__main__':
	# Calling main() function
	main()