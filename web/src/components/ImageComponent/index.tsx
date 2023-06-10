import React, {useState} from "react";
import { motion } from 'framer-motion';
import {ImageData} from "@/components/ImageComponent/Image.model";
import { useInView } from 'react-intersection-observer';

interface ImageComponentProps {
    image: ImageData;
}

const ImageComponent: React.FC<ImageComponentProps> = ({ image }) => {
    const [imageLoadError, setImageLoadError] = useState(false);
    const [isVisible, setIsVisible] = useState(false);
    const [ref, inView] = useInView({
        triggerOnce: true,
    });
    const handleImageLoad = () => {
        setIsVisible(true);
    };
    const handleImageError = () => {
        setImageLoadError(true);
    };
    if (!imageLoadError) {
        return <div ref={ref}>
            <motion.img
                src={inView ? image[0] : ''}
                alt={image[1]}
                width={800}
                height={800}
                onLoad={handleImageLoad}
                onError={handleImageError}
                style={{
                    opacity: isVisible ? 1 : 0,
                    transition: 'opacity 0.5s',
                }}
            />
        </div>;
    }
};
 export default ImageComponent