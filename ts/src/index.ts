export function add(a: number, b: number): number {
  return a + b;
}

if (require.main === module) {
  console.log('Hello from ts folder');
  console.log('3 + 4 =', add(3, 4));
}
