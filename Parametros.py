def best_parameters(land, level):
    if land == 1:
        if level == 1:
            du = 0.1
            tmp = 0.02
            num_p = 100
            fil = 0.7
            return du, tmp, num_p, fil
        elif level == 2:
            du = 0.1
            tmp = 0.02
            num_p = 20
            fil = 0.8
            return du, tmp, num_p, fil
        elif level == 3:                           
            du = 0.05
            tmp = 0.001
            num_p = 8
            fil = 0.7
            return du, tmp, num_p, fil
        elif level == 4:                           
            du = 0.01
            tmp = 0.001
            num_p = 100
            fil = 0.7
            return du, tmp, num_p, fil
    elif land == 2:
        if level == 1:
            du = 0.1
            tmp = 0.02
            num_p = 100
            fil = 0.8
            return du, tmp, num_p, fil
        elif level == 2:
            du = 0.1
            tmp = 0.01
            num_p = 10
            fil = 0.9
            return du, tmp, num_p, fil
        elif level == 3:
            du = 0.1
            tmp = 0.1
            num_p = 50
            fil = 0.7
            return du, tmp, num_p, fil
        elif level == 4:
            du = 0.1
            tmp = 0.1
            num_p = 50
            fil = 0.3
            return du, tmp, num_p, fil
    elif land == 3:
        if level == 1:
            du = 0.1
            tmp = 0.02
            num_p = 80
            fil = 0.6
            return du, tmp, num_p, fil
        elif level == 2:
            du = 0.1
            tmp = 0.1
            num_p = 20
            fil = 0.6
            return du, tmp, num_p, fil
        elif level == 3:
            du = 0.1
            tmp = 0.02
            num_p = 80
            fil = 0.95
            return du, tmp, num_p, fil
        elif level == 4:
            du = 0.1
            tmp = 0.3
            num_p = 50
            fil = 0.8
            return du, tmp, num_p, fil
    elif land == 4:
        if level == 1:
            du = 0.1
            tmp = 0.1
            num_p = 100
            fil = 0.6
            return du, tmp, num_p, fil
        elif level == 2:
            du = 0.1
            tmp = 0.1
            num_p = 100
            fil = 0.9
            return du, tmp, num_p, fil
        elif level == 3:
            du = 0.1
            tmp = 0.001
            num_p = 50
            fil = 0.7
            return du, tmp, num_p, fil
        elif level == 4:
            du = 0.1
            tmp = 0.02
            num_p = 50
            fil = 0.7
            return du, tmp, num_p, fil