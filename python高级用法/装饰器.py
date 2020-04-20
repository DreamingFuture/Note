def display_time(func):
	def wrapper():
		t1 = time.time()
		func()
		t2 = time.time()
		print(t2 - t1)


@display_time
def main():
    for i in range(1000):
        pass
    print('Hello world')

if __name__ == '__main__':
    main()