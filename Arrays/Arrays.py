class Array:
    def __init__(self,Max_Size=1):
        try:
            is_int_Size=int(Max_Size)
        except ValueError:
            raise ValueError("Please Enter Valid Size!")
            
        self._data=[None for i in range(is_int_Size)]
    
    def Insert(self,obj,Indx):
        if self.Index_Check(Indx):
            self._data[Indx]=obj
            print(f"Index: {Indx} Has Filled with {obj}")
        return None
    
    def Delete(self,Indx):

        if self.Index_Check(Indx):
            obj = self._data[Indx]
            self._data[Indx]=None
            return obj
        return None

    def Index_Check(self,Indx):
        try:
            is_int_Index=int(Indx)
        except ValueError:
            raise ValueError("Please Enter Valid Index!")
        if (is_int_Index <= len(self._data) - 1 ) and (is_int_Index >= 0) :
            return True
        raise IndexError("Index out of range!")