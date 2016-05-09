function borderMaker (imageFile)
% function to create 100 pixel transparent border around an image

borderSize = 150;

[img, ~, alpha] = imread(imageFile);

layer = img(:, :, 1);

[rows, cols] = size(layer);

vertArray = 255 * ones(borderSize, cols);
vertBorder = cat(3, vertArray, vertArray, vertArray);
img = [vertBorder; img; vertBorder];

horzArray = 255 * ones(rows + 2*borderSize, borderSize);
horzBorder = cat(3, horzArray, horzArray, horzArray);
img = [horzBorder, img, horzBorder];

alphaVertArray = zeros(borderSize, cols);
alpha = [alphaVertArray; alpha; alphaVertArray];
alphaHorzArray = zeros(rows + 2*borderSize, borderSize);
alpha = [alphaHorzArray, alpha, alphaHorzArray];

newImageName = [imageFile(1:end-4), '_border.png'];

imwrite(img, newImageName, 'Alpha', alpha);
    
end