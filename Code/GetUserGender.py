def getUserGender(list_of_users):
    import requests
    param='|'.join(list_of_users)
    
    
    url_new= 'https://en.wikipedia.org/w/api.php?action=query&format=json&list=users&usprop=gender&ususers={}'.format(param)
    data = requests.get(url_new).json()
    display = 'Name'+'\t'+'Gender\n'
    for item in data['query']['users']:
        print (item['name']+'\t'+item['gender'])
    return 