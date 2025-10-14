#Website Bookmarks: Design a system to store website bookmarks. What data structure would be most efficient for storing the URLs and their corresponding names, and for quickly retrieving a bookmark given its name?
#Use dictionary with tuple keys.
bookmark = {"默认书签页": ("roadmap", 'https://roadmap.sh/ai/course/python-data-structures-for-beginners-1747804470798')}

print(bookmark["默认书签页"])