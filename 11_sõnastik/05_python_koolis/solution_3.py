"""
Loo juurde kaks uut sõnastiku (e_inglise, e_itaalia), mille võti ei ole mitte eesti keeles, vaid vastavalt kas inglise või itaalia keeles.
Lisa sõnastikku ka kõik eelmises sõnastikus olevad sõnad.
"""
from solution_2 import est_eng_dict, est_ita_dict

def swap_dict_key_value(original_dict: dict[str, str]) -> dict[str, str]:
    result_dict = {}
    for key, value in original_dict.items():
        result_dict[value] = key
    return result_dict

eng_est_dict = swap_dict_key_value(est_eng_dict)
ita_est_dict = swap_dict_key_value(est_ita_dict)