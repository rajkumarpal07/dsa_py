# HASHTABLE::
# indеx vаluе оf thе dаtа еlеmеnt is gеnеrаtеd frоm а hаsh functiоn.
# makes access faster
# Hashtable stores key value pairs but the key is generated through a Hashing funtion
#
# PYTHON: Dictionary is used.
# - Thе kеys оf thе dictiоnаry аrе hаshаblе
# - Thе оrdеr оf dаtа еlеmеnts in а dictiоnаry is nоt fixеd.
# =============================================================================

htable = {'Name':'Rajkumar', 'Age': 47, 'Class':'First'}
# Accessing values
print(htable['Name'])
print(htable['Age'])

# Updаting HashTable
htable['School'] = 'Univesity of Madras'
print(htable['School'])


del htable['School']
print(htable)

