import sys
from bitarray import bitarray
from hashlib import sha1
import random
from random import randrange
import ipdb

class StableBloomFilter(object):
    """
    Class Methods for Probabilistic Duplicate Detection
    """
    
    def __init__(self,max,no_bits,d,k,P):
        """
        max -- Max Value of each element in a Cell
        no_bits -- Number of bits to be generated by a Hash Function !
        d -- No of bits in each element in a Cell
        """
        m = 2**no_bits
        self.d =d
        self.P = P #No of random cells to be chosen !
        self.total_size = m*d
        self.no_bits = no_bits
        self.no_hashes = k
        self.bitmap = bitarray(self.total_size)
        self.bitmap.setall(0)

    def _generate_parameters(self,fp_rate):
        """
        Generate Parameters given a FP Rate !!
        """

    def _check_cell(self,cell_no):
        """
        Check if all bits in a Cell are 0
        """
        return self.bitmap[cell_no:cell_no+d].any()

    def _decrement_cell(self,cell_no,d,val=1):
        """
        Decrement Cell by 'val'
        Recommended Default is '1'
        """
        cell_value = self.bitmap[cell_no:cell_no+d].to01()
        int_val = map()       
        
    def _update_cell(self,cell_no,d):
        """
        Updates the Cell of a Stable bloom Filter. Note that a Cell contains of 'd' elements
        """
        self.bitmap[cell_no:cell_no+d] = True

    def _choose_random_cells(self,P):
        """
        Returns Bucket Numbers of 'P' Random Celllls !!
        """
        generated_cells = {}        
        no_cells =0
        cell_list=[]
        while no_cells<P:
            rand_cell = randrange(0,self.total_size-1)
            if not generated_cells.get(rand_cell):
                no_cells+=1
                generated_cells[rand_cell]=True
                cell_list.append(rand_cell)
        return cell_list

    def _handle_data(self,text):
        """
        Handle A New Element Coming from a Stream. The Following Steps are done
        1) Randomly choose 'P' Cells and decrement
        """
        hash_buckets =[]
        dup_flag = True
        # Generate hash family functions
        for each in xrange(self.no_hashes):
            hash_val = self._gen_hash(each,text)
            # Probe each Cell
            dup_flag = dup_flag and self._check_cell(self.hash_val)
            hash_buckets.append(hash_val)  

        # Choose 'P' Different Cells !
        rand_cells = self._choose_random_cells(self.P)       
            
        

    def _gen_hash(self,seed_no,text):
        """
        Generate a 'n' bit Hash for a certain seed.
        """
        random.seed(seed_no)
        seed_bits = random.getrandbits(self.no_bits)
        hash_obj = sha1()
        hash_obj.update(text)
        hash_val = int(bin(int(hash_obj.hexdigest(),16))[2:self.no_bits+2],2)
        return hash_val ^ seed_bits

    def add(self,text):
        """
        Add an item to the Stable Bloom Filter !!
        """
        for each in xrange(self.no_hashes):
            cell_no = self._gen_hash(each,text)
            
            
        
    


if __name__=="__main__":
    ipdb.set_trace()
    ob = StableBloomFilter(5,24,10,7)
    print "Hello"
    
    


        
        

            
        

        




