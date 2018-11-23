query {
  noteList {
    edges {
      node {
        id
        author
        text
      }
    }
  }
}


mutation {
  createNote (input: {
    text: "Hello World!"
    author: "Correia"
  }) {
    note {
      id
      text
      author
    }
  }
}

mutation {
  updateNote (input:{
    id: "Tm90ZTo1MDkwMTYwMi1lZTk3LTExZTgtOTI3Yi0wODYyNjZiNTEwYTE="
    text: "d"
  }) {
    note {
      id
      text
      author
    }
  }
}

mutation {
  deleteNote (input:{
    id: "Tm90ZTo1MDkwMTYwMi1lZTk3LTExZTgtOTI3Yi0wODYyNjZiNTEwYTE="
  }) {
    note {
      text
    }
  }
}
