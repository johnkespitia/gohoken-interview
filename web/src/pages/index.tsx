import React from 'react';
import { getServerSideProps } from '@/services/client';
import ImageComponent from '@/components/ImageComponent';
import {removeDuplicates} from "@/services/utils";

interface HomeProps {
    data: [string, string][];
}

const Home: React.FC<HomeProps> = ({ data }) => {
    let dataFiltered = removeDuplicates(data)
    return (
        <main>
            <h1 className="text-4xl font-bold mb-6">Random Images!</h1>
            <div className="image-grid grid grid-cols-1 gap-4 sm:grid-cols-3">
                {dataFiltered.map((item: [string, string], index: number) => (
                    <ImageComponent image={item} key={index} />
                ))}
            </div>
        </main>
    );
};

export { getServerSideProps };
export default Home;
