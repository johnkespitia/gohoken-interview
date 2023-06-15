import React from 'react';
import { render, screen } from "@testing-library/react";
import '@testing-library/jest-dom/extend-expect';
import '@testing-library/jest-dom';
import 'intersection-observer';
import { removeDuplicates } from '@/services/utils';
import ImageComponent from '@/components/ImageComponent';
import Home from '@/pages';


describe('ImageComponent', () => {
    it('renders correctly', async () => {
        render(<ImageComponent image={['https://api.slingacademy.com/public/sample-photos/10.jpeg', 'Yard']} />);
        const image = await screen.findByAltText('Yard');
        await expect(image).toBeInTheDocument()
    });

    it('image not loaded', async () => {
        render(<ImageComponent image={['https://api.slingacademy.com/public/sample-photos/sad.jpeg', 'not loaded']} />);
        const image = await screen.findByAltText('not loaded');
        expect(image).toHaveAttribute('src', '');
    });
});

describe('removeDuplicates', () => {
    it('Remove Duplicates', () => {
        const param: [string, string][] = [['aaa', 'aaa'], ['bbb', 'bbb'], ['aaa', 'aaa']];
        const expected: [string, string][] = [['aaa', 'aaa'], ['bbb', 'bbb']];
        const data = removeDuplicates(param);
        expect(data).toStrictEqual(expected);
    });
});

describe('Home Component', () => {
    it('should render the correct title', () => {
        const data: [string, string][] = [['image1.jpg', 'description1'], ['image2.jpg', 'description2']];
        const { getByText } = render(<Home data={data} />);
        const titleElement = getByText('Random Images!');
        expect(titleElement).toBeInTheDocument();
    });
});
