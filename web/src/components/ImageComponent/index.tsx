import React, {useState} from "react";
import Image from 'next/image'
import {ImageData} from "@/components/ImageComponent/Image.model";

interface ImageComponentProps {
    image: ImageData;
}

const ImageComponent: React.FC<ImageComponentProps> = ({ image }) => {
    const [imageLoadError, setImageLoadError] = useState(false);

    const handleImageError = () => {
        setImageLoadError(true);
    };
    if (!imageLoadError) {
        return <Image src={image[0]} alt={image[1]} width={800} height={600} priority onError={handleImageError} />;
    }
};
 export default ImageComponent