from structures import CustomHashMap, LinkedQueue

class Parcel:
    def __init__(self, parcel_id, name, city, priority, status="Dispatched"):
        self.parcel_id = parcel_id
        self.name = name
        self.city = city
        # Priority: 1 = Urgent, 2 = High, 3 = Normal
        self.priority = int(priority)
        self.status = status

# Manual Implementation of Quick Sort O(n log n)
def quick_sort_parcels(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    
    # Sort primarily by priority rating (1 comes before 3)
    left = [x for x in arr if x.priority < pivot.priority]
    middle = [x for x in arr if x.priority == pivot.priority]
    right = [x for x in arr if x.priority > pivot.priority]
    
    return quick_sort_parcels(left) + middle + right

# Manual Implementation of Linear Search O(n)
def linear_search_parcels(arr, search_query, search_by="name"):
    results = []
    query = search_query.lower()
    for parcel in arr:
        if search_by == "name" and query in parcel.name.lower():
            results.append(parcel)
        elif search_by == "city" and query in parcel.city.lower():
            results.append(parcel)
    return results

# System Controller managing backend logic data flow
class TrackingSystem:
    def __init__(self):
        self.hash_map = CustomHashMap()
        self.delivery_queue = LinkedQueue()

    def register_parcel(self, parcel_id, name, city, priority):
        new_parcel = Parcel(parcel_id, name, city, priority)
        self.hash_map.put(parcel_id, new_parcel)
        self.delivery_queue.enqueue(new_parcel)

    def get_all_parcels(self):
        return self.hash_map.to_list()

    def find_by_id(self, parcel_id):
        return self.hash_map.get(parcel_id)

    def process_next_delivery(self):
        # Dequeue the oldest FIFO parcel from transit
        parcel = self.delivery_queue.dequeue()
        if parcel:
            parcel.status = "Delivered"
            # Update status inside the map registry
            self.hash_map.put(parcel.parcel_id, parcel)
            return parcel
        return None

    def get_priority_sorted_queue(self):
        raw_list = self.delivery_queue.to_list()
        return quick_sort_parcels(raw_list)