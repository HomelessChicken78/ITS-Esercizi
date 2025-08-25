import React from 'react'

const Clock = (props) => {
    console.log(props.timezone,props.country)
    const t=Date.now()+3600*props.timezone*1000;
    const new_time =  new Date(t)
    return (
        <h2>In {props.country} sono le {new_time.toLocaleTimeString()} del giorno {new_time.toLocaleDateString()}</h2>
    )
}