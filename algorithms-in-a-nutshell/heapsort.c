static void heapify (void **ar, int (*cmp)(const void *, const void *),
                     int idx, int max) {
  int left = 2*idx + 1;
  int right = 2*idx + 2;
  int largest;

  /* Find largest element of A[idx], A[left], and A[right]. */
  if (left < max && cmp (ar[left], ar[idx]) > 0) {
    largest = left;
  } else {
    largest = idx;
  }

  if (right < max && cmp (ar[right], ar[largest]) > 0) {
    largest = right;
  }

  /* If largest is not already the parent then swap and propagate. */
  if (largest != idx) {
    void *tmp;
    tmp = ar[idx];
    ar[idx] = ar[largest];
    ar[largest] = tmp;

    heapify (ar, cmp, largest, max);
   }
}

static void buildHeap (void **ar,
                       int (*cmp)(const void *, const void *), int n) {
  int i;
  for (i = n/2-1; i>=0; i--) {
    heapify (ar, cmp, i, n);
  }
}

void sortPointers (void **ar, int n,
                   int (*cmp)(const void *, const void *)) {
  int i;
  buildHeap (ar, cmp, n);
  for (i = n-1; i >= 1; i--) {
    void *tmp;
    tmp = ar[0];
    ar[0] = ar[i];
    ar[i] = tmp;

    heapify (ar, cmp, 0, i);
  }
}

int[] arr = [8, 11, 9, 2, 10, 16];
sortPointers(arr, 6);