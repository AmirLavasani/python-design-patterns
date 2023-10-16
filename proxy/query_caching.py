import time


# Define the interface for the Real Subject
class DatabaseQuery:
    def execute_query(self, query):
        pass


# Real Subject: Represents the actual database
class RealDatabaseQuery(DatabaseQuery):
    def execute_query(self, query):
        print(f"Executing query: {query}")
        # Simulate a database query and return the results
        return f"Results for query: {query}"


# Proxy: Caching Proxy for Database Queries
class CacheProxy(DatabaseQuery):
    def __init__(self, real_database_query, cache_duration_seconds):
        self._real_database_query = real_database_query
        self._cache = {}
        self._cache_duration = cache_duration_seconds

    def execute_query(self, query):
        if (
            query in self._cache
            and time.time() - self._cache[query]["timestamp"] <= self._cache_duration
        ):
            # Return cached result if it's still valid
            print(f"CacheProxy: Returning cached result for query: {query}")
            return self._cache[query]["result"]
        else:
            # Execute the query and cache the result
            result = self._real_database_query.execute_query(query)
            self._cache[query] = {"result": result, "timestamp": time.time()}
            return result


# Client code
if __name__ == "__main__":
    # Create the Real Subject
    real_database_query = RealDatabaseQuery()

    # Create the Cache Proxy with a cache duration of 5 seconds
    cache_proxy = CacheProxy(real_database_query, cache_duration_seconds=5)

    # Perform database queries, some of which will be cached
    print(cache_proxy.execute_query("SELECT * FROM table1"))
    print(cache_proxy.execute_query("SELECT * FROM table2"))
    time.sleep(3)  # Sleep for 3 seconds

    # Should return cached result
    print(cache_proxy.execute_query("SELECT * FROM table1"))

    print(cache_proxy.execute_query("SELECT * FROM table3"))
