
# needed for any cluster connection
from couchbase.cluster import Cluster
from couchbase.auth import PasswordAuthenticator

# options for a cluster and SQL++ (N1QL) queries
from couchbase.options import ClusterOptions, QueryOptions

# get a reference to our cluster
cluster = Cluster.connect('22fi4p7puvkvalyy.kzlwt6sd0zfe6pu6.cloud.couchbase.com', ClusterOptions(
  PasswordAuthenticator('team14', 'CFGteam14!'))) 

  