import React from 'react'
import AuthorList from './components/Author.js'
import BookList from './components/Book.js'
import AuthorBookList from './components/AuthorBook.js'
import LoginForm from './components/Auth.js'
import {BrowserRouter, Route, Switch, Redirect, Link} from 'react-router-dom'
import axios from 'axios'
import Cookies from 'universal-cookie';

const NotFound404 = ({location}) => {
    return (
        <div>
            <h1>Страница по адресу '{location.pathname}' не найдена</h1>
        </div>
    )
}

class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'authors': [],
            'books': [],
        }
    }

    get_headers() {
        let headers = {
            'Content-Type': 'application/json'
        }
        if (this.is_authenticated()) {
            headers['Authorization'] = 'Token ' + this.state.token
        }
        return headers
    }



    deleteBook(id) {
        axios.delete(`http://127.0.0.1:8000/api/books/${id}`)
            .then(response => {
                this.setState({
                    books: this.state.books.filter((item) => item.id !==
                        id)
                })
            }).catch(error => console.log(error))
    }


    load_data() {
        axios.get('http://127.0.0.1:8000/api/authors/')
            .then(response => {
                this.setState({authors: response.data})
            }).catch(error => console.log(error))
        axios.get('http://127.0.0.1:8000/api/books/')
            .then(response => {
                this.setState({books: response.data})
            }).catch(error => console.log(error))
    }


    componentDidMount() {
        this.load_data()
    }

    render() {
        return (
            <div className="App">
                <BrowserRouter>
                    <nav>
                        <ul>
                            <li>
                                <Link to='/'>Authors</Link>
                            </li>
                            <li>
                                <Link to='/books'>Books</Link>
                            </li>
                        </ul>
                    </nav>
                    <Switch>
                        <Route exact path='/' component={() => <AuthorList
                            items={this.state.authors}/>}/>
                        <Route exact path='/books' component={() => <BookList
                            items={this.state.books} deleteBook={(id) => this.deleteBook(id)}/>}/>
                        <Route path="/author/:id">
                            <AuthorBookList items={this.state.books}/>
                        </Route>
                        <Redirect from='/authors' to='/'/>
                        <Route component={NotFound404}/>
                    </Switch>
                </BrowserRouter>
            </div>
        )
    }
}

export default App
