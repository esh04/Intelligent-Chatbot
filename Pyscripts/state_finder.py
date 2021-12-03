state_list = ['andhra pradesh', 'arunachal pradesh', 'assam', 'bihar', 'chhattisgarh', 'goa', 'gujarat', 'haryana', 'himachal pradesh',
              'jammu and kashmir', 'jharkhand', 'karnataka', 'kerala', 'madhya pradesh', 'maharashtra', 'manipur',
              'meghalaya', 'mizoram', 'nagaland', 'odisha', 'punjab', 'rajasthan', 'sikkim', 'tamil nadu', 'telangana',
              'tripura', 'uttarakhand', 'uttar pradesh', 'west bengal', 'andaman and nicobar islands', 'chandigarh',
              'dadra and nagar haveli', 'daman and diu', 'delhi', 'lakshadweep', 'puducherry']


def state_finder(msg):
    msg_new = msg.lower()
    for i in state_list:
        if msg_new.find(i) != -1:
            break

    return i.title()

# state_finder("Stats for Arunachal Pradesh")
