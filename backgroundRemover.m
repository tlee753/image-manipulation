function backgroundRemover (inputFile)
% function to remove white backgrounds from images

image = imread(inputFile);
% reads in the input file in string format

outputString = [inputFile(1:end-4) '_clear.png'];
% creates the name of the output file by modifying input string

layer = image(:, :, 1);
% gets the first layer of the picture

[m, n] = size (layer);
% gets the size of the image

alphaArray = zeros (m, n);
% creates a vector of zeros equal in size to the image

alphaArray(layer <= 240) = 1;
% assigns value of 1 to any pixel that isn't white
% keeps pixel from being transparent

imwrite (image, outputString, 'Alpha', alphaArray);
% writes output with white pixels being transparent

end

% http://stackoverflow.com/questions/10213320/make-a-pixel-transparent-in-matlab

% alphaArray = zeros(size(X));
% alphaArray(X == 255) = 1;

% for i = 1:m
%     for j = 1:n
%         if image(i, j) == 255
%             alphaArray(i, j) = 1;
%         end
%     end
% end