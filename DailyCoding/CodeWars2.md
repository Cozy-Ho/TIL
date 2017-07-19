CodeWars_2
===========
# Question
You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items.  
We want to create the text that should be displayed next to such an item.  
  
Implement a function `likes :: [String] -> String` , which must take in input array,  
containing the names of people who like an item. It must return the display text as shown in the examples:
```{.Python}
likes [] // must be "no one likes this"
likes ["Peter"] // must be "Peter likes this"
likes ["Jacob", "Alex"] // must be "Jacob and Alex like this"
likes ["Max", "John", "Mark"] // must be "Max, John and Mark like this"
likes ["Alex", "Jacob", "Mark", "Max"] // must be "Alex, Jacob and 2 others like this"
```
For more than 4 names,the number in `and 2 others`simply increases.  

>페이스북의 "좋아요" 시스템을 흉내내는 프로그램이다.
>나름 쉬워서 보자마자 작성했다.

## My Solution
```{.Python}
def likes(names):
	l = len(names)
	if l==0:
		return 'no on likes this'
	slif l<2:
		return names[0]+' likes this'
	elif l<3:
		return names[0]+' and '+names[1]+' like this'
	elif l<4:
		return names[0]+', '+names[1]+' and '+names[2]+' like this'
	else:
		return names[0]+', '+names[1]+' and ' +str(l-2)+' others'+' like this'
```

## JerryB's Solution
```{.Python}
def likes(names):
	n = len(names)
	return {
		0: 'no one likes this',
		1: '{} likes this', 
		2: '{} and {} like this', 
		3: '{}, {} and {} like this', 
		4: '{}, {} and {others} others like this'
	}[min(4, n)].format(*names[:3], others=n-2)
```

리스트 수정을 이렇게 고급지게 하다니!  
format 사용법을 배우긴했지만 이렇게 사용한다는걸 깨달았다.
~~(공부좀 더하자..)~~  
각각 실행해보니 내 방법보다  속도도 더 빠르다!  

        
