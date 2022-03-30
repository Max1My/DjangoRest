import React from 'react'
import { useParams } from 'react-router-dom'

const UserItem = ({item}) => {
    return (
        <tr>
            <td>{item.id}</td>
            <td>{item.name}</td>
            <td>{item.project.name}</td>
        </tr>
    )
}

const ProjectUserList = ({items}) => {
    let { id } = useParams();
    let filtered_items = items.filter((item) => item.project.id == id)
    return (
        <table>
            <tr>
                <th>ID</th>
                <th>USERNAME</th>
                <th>PROJECT</th>
            </tr>
            {filtered_items.map((item) => <UserItem item={item} />)}
        </table>
    )
}

export default ProjectUserList