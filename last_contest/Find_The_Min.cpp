#include <iostream>
#include <queue>
#include <unordered_map>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int Q;
    cin >> Q;

    priority_queue<int, vector<int>, greater<int>> min_heap;
    unordered_map<int, int> count_map;

    while (Q--) {
        int query;
        cin >> query;

        if (query == 1) {
            int X;
            cin >> X;
            min_heap.push(X);
            count_map[X]++;
        } else if (query == 2) {
            if (min_heap.empty()) {
                cout << "empty" << "\n";
            } else {
                // Get the minimum element
                while (!min_heap.empty()) {
                    int min_value = min_heap.top();
                    // Check if this minValue is still valid (exists in count_map)
                    if (count_map[min_value] > 0) {
                        cout << min_value << "\n"; // Output the minimum value
                        count_map[min_value] = 0; // Erase all occurrences
                        min_heap.pop(); // Remove from heap
                        break; // Exit after printing and erasing
                    } else {
                        min_heap.pop(); // Remove stale entries
                    }
                }
            }
        }
    }
    return 0;
}
