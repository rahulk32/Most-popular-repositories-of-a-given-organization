import requests
print('Enter organization name in small letters :')
Org=input()
print('Enter vaue of n :')
n=int(input())
print('Enter value of m :')
m=int(input())

# Retrieve repositories data of provided organization using get request with github api
def get_repos():
    res=requests.get('https://api.github.com/orgs/ORG/repos', {'org': Org})
    return res.json()

repo = get_repos()

#sort the repositories according to number of forks of repositories
result = sorted(repo, key=lambda repo: repo['forks_count'],reverse = True)

#convert the values into a list(li) for easily accessibile
li=list(result)
if n>len(li):
     print('Entered value of n is greater than no. of repositories of organization')
     print('Count of available repositories =>  ',len(li))
     print('')
     n=len(li)
     
for i in range(0,n):
    url=li[i]['url']
    print((i+1),end='')
    print('th repository according to fork count  => ',li[i]['html_url'])#ith popular repo
    print('fork count =>  ',li[i]['forks'])
    #sort committes based on number of commits in repository
    Committes=requests.get(url+'/contributors'+'?q=commits&order=desc').json()
    cnt=0
    if m>len(Committes):
        print('Entered value of m is greater than no. of committees for above repository')
        print('Count of Committees for above repository  => ',len(Committes))
    print('top m committees for',end=' ')
    print((i+1),end='')
    print('th repository =>  ')
    if m>len(Committes):
        m1=len(Committes)
        print('Above repository has total',end=' ')
        print(m1,end=' ')
        print('Committees =>')
    else:
        m1=m
    for committe in Committes:
        if cnt==m1:
            break
        print(committe['html_url'])#committes for above repository 
        cnt+=1
    print('')
    
    
# Here n is refered for n most popular repositories based on the number of forks
# m is refered top m committes based on number of commits for each 
# repository of top n repositories of organization
   