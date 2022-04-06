import React from 'react'
import {Link, useParams} from "react-router-dom";


const UserItem = ({item}) => {
    return (
        <tr>
            <td>{item.id}</td>
            <td>{item.username}</td>
            <td>{item.project.name}</td>
        </tr>
    )
}
const UserList = ({items}) => {
    return (
        <table>
            <tr>
                <th>ID</th>
                <th>USERNAME</th>
                <th>PROJECT</th>
            </tr>
            {items.map((item) => <UserItem item={item}/>)}
        </table>
    )
}



export default UserList