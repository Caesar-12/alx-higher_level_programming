#include "hash_tables.h"

/**
 * hash_table_create - Creates an hash table
 *
 * @size: Sizeof hash table to be created
 * Return: Hash table
 */

hash_table_t *hash_table_create(unsigned long int size)
{
	hash_table_t *ht_entry;
	unsigned long int trav;

	ht_entry = (hash_table_t *)malloc(sizeof(hash_table_t *) * size);

	for (trav = 0; trav < size; trav++)
		ht_entry->array = NULL;

	return (ht_entry);
}
