class Palindrome:
    def is_Palindrome(self,x):
        is_polindrome=True
        is_odd=True
        x_str=str(x)
        x_len=len(x_str)
        i=0
        j=x_len-1
        if x_len%2==0:
            is_odd=False

        if is_odd:
            while i<=j:
                if x_str[i]==x_str[j]:
                    i=i+1
                    j=j-1
                else :
                    is_polindrome=False
                    break
        else:
            while i<j:
                if x_str[i] == x_str[j]:
                    i = i + 1
                    j = j - 1
                else:
                    is_polindrome = False
                    break

        return is_polindrome

if __name__=="__main__":
    pp=Palindrome()
    res=pp.is_Palindrome('{:+}'.format(848))
    if res:
        print("Yes it is Polindrome")
    else:
        print("No it is not Polindrome")