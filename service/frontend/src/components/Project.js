import React from 'react'
import {Link} from 'react-router-dom'

const ProjectItem = ({item}) => {
    return (
        <tr>
            <td><Link to={`project/${item.id}`}>{item.id}</Link></td>
            <td>{item.name}</td>
            <td>{item.links_repo}</td>
        </tr>
    )
}

const ProjectList = ({items}) => {
    return (
        <table>
            <tr>
                <th>ID</th>
                <th>NAME</th>
                <th>LINKS</th>
            </tr>
            {items.map((item) => <ProjectItem item={item}/>)}
        </table>
    )
}
export default ProjectList