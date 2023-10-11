import numpy as np
import pandas

class BitcoinLoader:  
    def __init__(
        self,
        input_path: str
    ) -> None:
        self.dataset = pandas.read_csv(input_path)
        self.num_nodes = 5881
        self.num_edges = 35592
        self.transform_from_raw()
    
    def transform_from_raw(self) -> None:
        self.dataset['source'] = self.dataset['source'] - 1
        self.dataset['target'] = self.dataset['target'] - 1
        self.dataset['time'] = self.dataset['time'] - 1289241910.7283599376678467
        missing_ids = [10, 11, 13, 17, 21, 23, 26, 29, 37, 39, 41, 42, 47, 48, 49, 57, 58, 62, 66, 72, 81, 83, 84, 89, 90, 91, 97, 101, 116, 117, 120, 122, 123, 125, 127, 129, 135, 150, 225, 567, 1338, 1397, 1562, 1637, 1651, 1995, 2074, 2293, 2360, 2456, 2466, 2553, 2559, 2582, 2649, 2763, 2841, 2950, 2956, 2966, 2978, 3003, 3006, 3013, 3038, 3056, 3151, 3185, 3338, 3349, 3355, 3401, 3460, 3529, 3637, 3808, 3832, 4008, 4020, 4192, 4193, 4222, 4259, 4271, 4331, 4499, 4509, 4560, 4574, 4816, 4826, 5101, 5265, 5492, 5508, 5534, 5561, 5571, 5583, 5619, 5620, 5627, 5636, 5650, 5670, 5689, 5695, 5696, 5715, 5726, 5727, 5733, 5734, 5750, 5757, 5770, 5786, 5793, 5811, 5833, 5840, 5841, 5864, 6000]
        def return_list_spot(list, value: int):
            temp_list = list[:] + [value]
            temp_list.sort()
            return temp_list.index(value)
        self.dataset['source'] = self.dataset['source'].apply(lambda x: x - return_list_spot(missing_ids, x))
        self.dataset['target'] = self.dataset['target'].apply(lambda x: x - return_list_spot(missing_ids, x))

    @property
    def cols(self):
        return self.dataset.columns