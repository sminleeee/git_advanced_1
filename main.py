from typing import List

def even_list(int_list: List[int]) -> List[int]:
    res_list=[]
    for i in List:
        if i%2==0:
            res_list.append(i)
    
    return res_list
    

    
def sum_of_squares_of_even(even_int_list: List[int]) -> int:
    
    
    
# Main function
def main():
    # Example list
    int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_int_list = even_list(int_list)
    output = sum_of_squares_of_even(even_int_list)
    print(output)
    
# Boilerplate code
if __name__ == "__main__":
    main()