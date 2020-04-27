import re
match_list_fir = ["mg", "kg", "g", "ms", "s", "h","m"]
match_list_fir = ["[1-9]+[\.][0-9]+" + x for x in match_list_fir] + ["[1-9]+[0-9]*" + x for x in match_list_fir]
match_list_fir = ["\d+h"] + match_list_fir
input_str = "10mgs09h80s777jig7ms7.8mg10..ms8.ms"
out_str_list_fir = re.findall("|".join(match_list_fir), input_str)
print(out_str_list_fir)