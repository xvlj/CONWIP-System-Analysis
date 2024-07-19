import numpy as np

# Define the variables as NumPy arrays
w_1 = np.float64(6)
w_2 = np.float64(10)
st_1 = np.array([1/2,3/4,4/5])
st_2 = np.array([8/5,6/5,1/2])
r_1 = np.array([1, 0.8095, 0.5714])
r_2 = np.array([1, 0.5375, 0.66875])
ct_1 = np.array([1/2,3/4,4/5])
th_1 = np.zeros(3)
ct_2 = np.array([8/5,6/5,1/2])
th_2 = np.zeros(3)

for i in range(1,13):
	
	# Calculate ct_sum
	ct_1_sum = np.dot(r_1, ct_1)
	ct_2_sum = np.dot(r_2,ct_2)
	
	# Calculate ct
	ct_1 = st_1 + st_1 * (((w_1-1)*r_1*ct_1)/ct_1_sum) + st_2 * ((w_2*r_2*ct_2)/ct_2_sum)
	
	ct_2 = st_2 + st_2 * (((w_2-1)*r_2*ct_2)/ct_2_sum) + st_1 * ((w_1*r_1*ct_1)/ct_1_sum)

	# Calculate th and update wip
	th_1 = (r_1 * w_1) / ct_1_sum
	th_2 = (r_2 * w_2) / ct_2_sum
	wip_1 = th_1 * ct_1
	wip_2 = th_2 * ct_2
	print("iteration:", i)
	print("workstation measures")
	print("CT", )
	print("TH_1", th_1+th_2)
	print("WIP_1", wip_1+wip_2)
	print("Util", (st_1*th_1)+(st_2*th_2))
	print("system measures:")
	th_s = th_1[2]*.75+th_2[2]*.8
	print("CT", (w_1+w_2)/th_s)
	print("TH", th_s)
	print("WIP", w_1+w_2)
	print('------------------')
