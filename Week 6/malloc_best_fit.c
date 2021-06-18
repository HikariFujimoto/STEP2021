#include <assert.h>
#include <math.h>
#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/mman.h>
#include <sys/time.h>

void* mmap_from_system(size_t size);
void munmap_to_system(void* ptr, size_t size);

typedef struct metadata_t {
  size_t size;
  struct metadata_t* next;
} metadata_t;

typedef struct heap_t {
  metadata_t* free_head;
  metadata_t dummy;
} heap_t;

heap_t heap;

// Add a free slot to the beginning of the free list.
void add_to_free_list(metadata_t* metadata) {
  assert(!metadata->next);
  metadata->next = heap.free_head;
  heap.free_head = metadata;
}

// Remove a free slot from the free list.
void remove_from_free_list(metadata_t* metadata, metadata_t* prev) {
  if (prev) {
    prev->next = metadata->next;
  } else {
    heap.free_head = metadata->next;
  }
  metadata->next = NULL;
}

// This is called only once at the beginning of each challenge.
void my_initialize() {
  heap.free_head = &heap.dummy;
  heap.dummy.size = 0;
  heap.dummy.next = NULL;
}

void* my_malloc(size_t size) {
  metadata_t* metadata = heap.free_head;
  metadata_t* prev = NULL;
  // best-fit: Find the smallest free slot the object fits.
  size_t diff = 4097;
  metadata_t* best_fit = NULL;
  metadata_t* prev_best_fit = NULL;
  while (metadata) {
    if (metadata->size >= size && (metadata->size - size) < diff) {
      diff = metadata->size - size;
      prev_best_fit = prev;
      best_fit = metadata;
    }
    prev = metadata;
    metadata = metadata->next;
  }

  if (best_fit) {
    prev = prev_best_fit;
    metadata = best_fit;
  }

  if (!metadata) {
    size_t buffer_size = 4096;
    metadata_t* metadata = (metadata_t*)mmap_from_system(buffer_size);
    metadata->size = buffer_size - sizeof(metadata_t);
    metadata->next = NULL;
    add_to_free_list(metadata);
    return my_malloc(size);
  }

  void* ptr = metadata + 1;
  size_t remaining_size = metadata->size - size;
  metadata->size = size;
  // Remove the free slot from the free list.
  remove_from_free_list(metadata, prev);

  if (remaining_size > sizeof(metadata_t)) {
    metadata_t* new_metadata = (metadata_t*)((char*)ptr + size);
    new_metadata->size = remaining_size - sizeof(metadata_t);
    new_metadata->next = NULL;
    add__to_free_list(new_metadata);
  }
  return ptr;
}

void my_free(void* ptr) {
  metadata_t* metadata = (metadata_t*)ptr - 1;
  add__to_free_list(metadata);
}

void my_finalize() {}

void test() {}