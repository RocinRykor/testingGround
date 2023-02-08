from sheaf_generator import security_sheaf

if __name__ == '__main__':
    test = security_sheaf.generate_sheaf(1, 7)

    print("Printing Sheaf!  (Step: Event)")
    for step in test:
        print(step)
