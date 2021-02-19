def numUniqueEmails(self, emails):
    """
    :type emails: List[str]
    :rtype: int
    """
    email_set = set()
    for i in emails:
        email = i.split("@")
        local = email[0].replace(".", "")
        locate_plus = local.find("+")
        if locate_plus != -1:
            email_set.add(local[:locate_plus] + "@" + email[1])
        else:
            email_set.add(local + "@" + email[1])
    return len(email_set)

#Less efficient
#         hash_map = {}
#         for i in emails:
#             locate_at = i.find("@")
#             local = get_rid_periods(i[:locate_at])
#             locate_plus = local.find("+")
#             if locate_plus != -1 and locate_plus < locate_at:
#                 email = local[:locate_plus] + i[locate_at:]
#                 if email not in hash_map:
#                     hash_map[email] = 0
#                 else:
#                     pass
#             else:
#                 email = local + i[locate_at:]
#                 if email not in hash_map:
#                     hash_map[email] = 0
#                 else:
#                     pass
#         return len(hash_map)


# def get_rid_periods(local_name):
#     return "".join([i for i in local_name if i != "."])

Input = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
# Output: 2
# Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails