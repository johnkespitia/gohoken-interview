const  getServerSideProps = async () => {
    try{
    const response = await fetch(`${process.env.API_URL}/images`);
    const data = await response.json();
    return {
        props: {
            data,
        },
    };
    }catch (e) {
        return {
            props: {
                data: null,
            },
        }
    }
}

export {getServerSideProps}