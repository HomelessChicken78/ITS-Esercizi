import React, { useState, useEffect } from 'react'
import axios from "axios"

const useFetch = (url) => {

    const [data, setData] = useState([])
    const [isLoading, setIsLoading] = useState(true)

    useEffect(() => {
        (async () => {
            setIsLoading(true)
            try {
                const response = axios.get(url);
                setData(response.data)
            } catch (err) {
                console.log(err)
            }
            setIsLoading(true)
        })()
    }, [url])

    return { data, isLoading }
}

export default useFetch