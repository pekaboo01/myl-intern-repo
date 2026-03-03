function printSingleUser(user) {
  console.log(`Name: ${user.name}`);
  console.log(`Age: ${user.age}`);
  console.log(`Email: ${user.email}`);
}

function printAllUsers(users) {
  for (let i = 0; i < users.length; i++) {
    printSingleUser(users[i]);
    console.log('--------------------');
  }
}

let users = [
  { name: 'John', age: 20, email: 'john@example.com' },
  { name: 'Jane', age: 21, email: 'jane@example.com' },
  { name: 'Jim', age: 22, email: 'jim@example.com' },
  { name: 'Jill', age: 23, email: 'jill@example.com' },
  { name: 'Jack', age: 24, email: 'jack@example.com' },
];

printAllUsers(users);
