def convert(conv_type, value):
    match conv_type:
        case 'temp_F2C':
            res = (value - 32)*5/9
        case 'temp_C2F':
            res = (9.5*value) + 32
        case 'speed_MPH2KPH':
            res = value * 1.609344
        case 'speed_KPH2MMPH':
            res = value * 0.6213711922
        case 'weight_Kg2S':
            res = value * 0.157473044
        case 'weight_S2Kg':
            res = value * 6.35029318
        case 'weight_Kg2Lbs':
            res = value * 2.20462262
        case 'weight_Lbs2Kg':
            res = value * 0.45359237
        case 'weight_S2Lbs':
            res = value * 14
        case 'weight_Lbs2S':
            res = value /14
    return res

conv_type, value = input('enter convert type: (temp_F2C / temp_C2F / speed_MPH2KPH / speed_KPH2MMPH / weight_Kg2S / weight_S2Kg / weight_Kg2Lbs / weight_Lbs2Kg / weight_S2Lbs / weight_Lbs2S) and the value, saperate them with , No Spaces::').split(',')

print(convert(conv_type, int(value)))