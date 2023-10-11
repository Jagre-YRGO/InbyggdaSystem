print('Beräknar differensen av jämna/udda tal...')

even_numbers = list(range(2,2002,2))
odd_numbers = list(range(1,2000,2))

diff = sum(even_numbers) - sum(odd_numbers)

print(f'Differensen={diff}')
