import React from 'react'
import AuthorList from './components/Author.js'
import ProjectList from "./components/Project";
import BookList from './components/Book.js'
import UserList from "./components/User";
import ToDoList from "./components/ToDoList";
import {HashRouter, Route,Link, Switch, Redirect,BrowserRouter} from "react-router-dom";
import AuthorBookList from "./components/AuthorBook";
import Project from "./components/Project";
import ProjectUserList from "./components/ProjectUser";

const NotFound404 = ({ location }) => {
    return (
        <div>
            <hi>Страница по адресу `{location.pathname}` не найдена :( </hi>
        </div>
    )
}

class App extends React.Component {
    constructor(props) {
        super(props)
        const project1 = {id: 1, name: 'Django', links_repo: 'https://github.com/Max1My'}
        const project2 = {id: 2, name: 'Android', links_repo: 'https://github.com/Max1My'}
        const projects = [project1, project2]
        const user1 = {id: 1, name: 'maximy', project: project1}
        const user2 = {id: 2, name: 'john', project: project1}
        const user3 = {id: 3, name: 'Victor', project: project2}
        const user4 = {id: 4, name: 'Alex', project: project2}
        const users = [user1, user2, user3, user4]
        const commit1 = {id:1, project:project1,user:user1,text:'fix bug'}
        const commit2 = {id:2, project:project1,user:user2,text:'create new app'}
        const commit3 = {id:3, project:project2,user:user3,text:'add button'}
        const commit4 = {id:4, project:project2,user:user4,text:'fix bug'}
        const commit5 = {id:5, project:project1,user:user2,text:'fix bug'}
        const todolist = [commit1,commit2,commit3,commit4,commit5]
        this.state = {
            'projects': projects,
            'users': users,
            'todolist':todolist
        }
    }

    render() {
        return (
            <div className="App">
                <BrowserRouter>

                    <nav>
                        <ul>
                            <li>
                                <Link to='/'>Projects</Link>
                            </li>
                            <li>
                                <Link to='/users'>Users</Link>
                            </li>
                            <li>
                                <Link to='/todo'>ToDo</Link>
                            </li>
                        </ul>
                    </nav>
                    <Switch>
                        <Route exact path={'/'} component={() => <ProjectList
                        items={this.state.projects}/>}/>
                        <Route exact path={'/users'} component={() => <UserList
                        items={this.state.users}/>} />
                        <Route exact path={'/todo'} component={() => <ToDoList
                        items={this.state.todolist}/>} />
                        <Route path="/project/:id">
                            <ProjectUserList items={this.state.users}/>
                        </Route>
                        <Redirect from='/projects' to='/'/>
                        <Route component={NotFound404}/>
                    </Switch>
                </BrowserRouter>
            </div>
        )
    }
}

export default App;