#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # check_dict = {}

        # for ch in s:
        #     if ch not in check_dict:
        #         check_dict[ch] = 1
        #     else:
        #         check_dict[ch] += 1

        # for ch in t:
        #     if ch not in check_dict:
        #         return False
            
        #     else:
        #         if check_dict[ch] < 1:
        #             return False
        #         else:
        #             check_dict[ch] -= 1
        
        # for k, v in check_dict.items():
        #     if v != 0:
        #         return False
            
        # return True


        check_dict_s = {}
        for ch in s:
            if ch not in check_dict_s:
                check_dict_s[ch] = 1
            else:
                check_dict_s[ch] += 1

        check_dict_t = {}
        for ch in t:
            if ch not in check_dict_t:
                check_dict_t[ch] = 1
            else:
                check_dict_t[ch] += 1


        return check_dict_t == check_dict_s

        
    
# @lc code=end

